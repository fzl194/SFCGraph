---
id: UNC@20.15.2@ConfigObject@NGAREARESELPLCY
type: ConfigObject
name: NGAREARESELPLCY（AMF区域重选控制策略）
nf: UNC
version: 20.15.2
object_name: NGAREARESELPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGAREARESELPLCY（AMF区域重选控制策略）

## 说明

![](增加AMF区域重选控制策略（ADD NGAREARESELPLCY）_70462513.assets/notice_3.0-zh-cn_2.png)

“区域范围”指定为“所有区域”或者“控制对象”指定为“无签约信息”的配置方式建议只在园区AMF设备使用，避免误配置导致非园区用户被误重路由，导致用户业务受损。

**适用NF：AMF**

该命令用于增加AMF区域重选功能控制策略。AMF可基于当前用户的位置以及号段和签约切片等信息，控制是否需要将用户通过重路由方式重选至指定的AMF组。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户请求通过RAN重定向给园区AMF；园区AMF可以通过本地配置将大网用户请求通过基站重定向给大网AMF。大网和园区以及园区（如园区1、园区2）之间共享RAN且园区1、2和大网失联时，园区1的AMF可以通过本地配置将园区2的用户请求通过RAN重定向到园区2的AMF; 园区2的AMF可以通过本地配置将园区1的用户请求通过RAN重定向到园区1的AMF。

## 操作本对象的命令

- [ADD NGAREARESELPLCY](command/UNC/20.15.2/ADD-NGAREARESELPLCY.md)
- [LST NGAREARESELPLCY](command/UNC/20.15.2/LST-NGAREARESELPLCY.md)
- [MOD NGAREARESELPLCY](command/UNC/20.15.2/MOD-NGAREARESELPLCY.md)
- [RMV NGAREARESELPLCY](command/UNC/20.15.2/RMV-NGAREARESELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF区域重选控制策略（MOD-NGAREARESELPLCY）_23622978.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF区域重选控制策略（RMV-NGAREARESELPLCY）_70382377.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF区域重选控制策略（ADD-NGAREARESELPLCY）_70462513.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF区域重选控制策略（LST-NGAREARESELPLCY）_70462549.md`
