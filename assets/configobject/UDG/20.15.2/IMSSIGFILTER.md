---
id: UDG@20.15.2@ConfigObject@IMSSIGFILTER
type: ConfigObject
name: IMSSIGFILTER（IMS分类器）
nf: UDG
version: 20.15.2
object_name: IMSSIGFILTER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# IMSSIGFILTER（IMS分类器）

## 说明

**适用NF：PGW-U、UPF**

![](添加IMS分类器（ADD IMSSIGFILTER）_82837817.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认添加规则后合法的IMS信令报文都能命中其中一条规则。

该命令用于增加系统整机的IMS信令专用上下文的分类器配置。当运营商规划IMS网络时，使用该命令增加IMS专用上下文的分配器。IMS网络可以为用户提供丰富多彩的基于Internet应用统一的多媒体业务和应用，如语音业务、实时多媒体业务和视频会议等。

## 操作本对象的命令

- [ADD IMSSIGFILTER](command/UDG/20.15.2/ADD-IMSSIGFILTER.md)
- [LST IMSSIGFILTER](command/UDG/20.15.2/LST-IMSSIGFILTER.md)
- [MOD IMSSIGFILTER](command/UDG/20.15.2/MOD-IMSSIGFILTER.md)
- [RMV IMSSIGFILTER](command/UDG/20.15.2/RMV-IMSSIGFILTER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IMS分类器（MOD-IMSSIGFILTER）_82837818.md`
- 原始手册：`evidence/UDG/20.15.2/删除IMS分类器（RMV-IMSSIGFILTER）_86526216.md`
- 原始手册：`evidence/UDG/20.15.2/查询IMS分类器（LST-IMSSIGFILTER）_82837820.md`
- 原始手册：`evidence/UDG/20.15.2/添加IMS分类器（ADD-IMSSIGFILTER）_82837817.md`
