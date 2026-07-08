---
id: UNC@20.15.2@MMLCommand@RMV NGNILRPARA
type: MMLCommand
name: RMV NGNILRPARA（删除NI-LR功能参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGNILRPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G定位服务管理
- 紧急定位服务管理
status: active
---

# RMV NGNILRPARA（删除NI-LR功能参数）

## 功能

**适用NF：AMF**

该命令用于基于运营商删除NI-LR功能的参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于在UNC系统内唯一标识移动网络运营商。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：<br>该参数取值必须和ADD NGMNO中配置的“NOID”参数取值相同。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGNILRPARA]] · NI-LR功能参数（NGNILRPARA）

## 使用实例

删除NOID为0的运营商的NI-LR功能参数，执行如下命令:

```
RMV NGNILRPARA:NOID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGNILRPARA.md`
