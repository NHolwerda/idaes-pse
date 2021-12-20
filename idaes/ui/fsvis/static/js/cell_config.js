/**
 * The Institute for the Design of Advanced Energy Systems Integrated Platform
 * Framework (IDAES IP) was produced under the DOE Institute for the
 * Design of Advanced Energy Systems (IDAES), and is copyright (c) 2018-2021
 * by the software owners: The Regents of the University of California, through
 * Lawrence Berkeley National Laboratory,  National Technology & Engineering
 * Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia University
 * Research Corporation, et al.  All rights reserved.
 *
 * Please see the files COPYRIGHT.md and LICENSE.md for full copyright and
 * license information.
*/

/**
 * Interpret cell configuration specified by each icon chosen in the model.
 * Configuring cell parameters such as the routing paths that are taken by
 * links connecting unit models.
 */
export class JointJsCellConfig {
	constructor(model) {
	    this._model = model;
	}
    
	get model() {
	    return this._model
	}
    
	set model(model) {
	    this._model = model;
	}

    /**
     * Generate a custom function that handles the router 'gap' option.
     * The 'gap' option is specified by the users to choose the two vertices
     * that the link will take to connect the unit models (elements).
    */
     routerGapFnFactory(gap) {
        var router_fn = (vertices, opt, linkView) => {
            const a = linkView.getEndAnchor('source');
            const b = linkView.getEndAnchor('target');
            const p1 = {
                x: a.x + gap.source.x,
                y: a.y + + gap.source.y
            };
            const p2 = {
                x: b.x + gap.destination.x,
                y: b.y + gap.destination.y
            };

            // TODO: Research if there's a better pre-implemented router
            // function than the manhattan function.
            return joint.routers.manhattan([p1, ...vertices, p2], opt, linkView);
        }

        return router_fn;
    }

	processRoutingConfig() {
        const src = "source";
        const dest = "destination";

        var routing_config = this._model['routing_config'];
        for (var link in routing_config) {
            var routing_fn = this.routerGapFnFactory(
                routing_config[link].cell_config.gap
            );

            this._model['cells'][routing_config[link].cell_index].router = routing_fn;
        }
        return this._model;
	}
};
