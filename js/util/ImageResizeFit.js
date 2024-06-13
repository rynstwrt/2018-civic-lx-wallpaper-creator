class ImageResizeFit
{
    static #cover = 0;
    static #contain = 1;
    static #fill = 2;
    static #inside = 3;
    static #outside = 4;

    static get cover () { return this.#cover }
    static get contain () { return this.#contain }
    static get fill () { return this.#fill }
    static get inside () { return this.#inside }
    static get outside () { return this.#outside }
}


module.exports = ImageResizeFit;