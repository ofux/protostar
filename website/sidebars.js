/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorials: [
    {
      type: 'doc',
      id: 'tutorials/introduction',
    },
    {
      type: 'doc',
      id: 'tutorials/installation',
    },
    {
      type: 'doc',
      id: 'tutorials/project-initialization',
    },
    {
      type: 'category',
      label: 'Guides',
      items: [{ type: 'autogenerated', dirName: 'tutorials/guides' }],
    },
  ],
}

module.exports = sidebars
