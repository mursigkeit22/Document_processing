# return _Footer(self._sectPr, self._document_part, WD_HEADER_FOOTER.PRIMARY)

# @property
#     def _definition(self):
#         """|FooterPart| object containing content of this footer."""
#         footerReference = self._sectPr.get_footerReference(self._hdrftr_index)
#         return self._document_part.footer_part(footerReference.rId)
#     def add_relationship(self, reltype, target, rId, is_external=False):
#         """
#         Return a newly added |_Relationship| instance.
#         """
#         rel = _Relationship(rId, reltype, target, self._baseURI, is_external)
#         self[rId] = rel
#         if not is_external:
#             self._target_parts_by_rId[rId] = target
#         return rel


# @property
#     def _next_rId(self):
#         """
#         Next available rId in collection, starting from 'rId1' and making use
#         of any gaps in numbering, e.g. 'rId2' for rIds ['rId1', 'rId3'].
#         """
#         for n in range(1, len(self)+2):
#             rId_candidate = 'rId%d' % n  # like 'rId19'
#             if rId_candidate not in self:
#                 return rId_candidate


# @property
#     def target_ref(self):
#         if self._is_external:
#             return self._target
#         else:
#             return self._target.partname.relative_ref(self._baseURI)