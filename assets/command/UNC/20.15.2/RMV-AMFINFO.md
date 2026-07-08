---
id: UNC@20.15.2@MMLCommand@RMV AMFINFO
type: MMLCommand
name: RMV AMFINFO（删除AMF信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF信息管理
status: active
---

# RMV AMFINFO（删除AMF信息）

## 功能

![](删除AMF信息（RMV AMFINFO）_09653047.assets/notice_3.0-zh-cn_2.png)

执行该命令将触发AMF到NRF的属性同步流程，导致本AMF无法被其它NF发现和选择，从而影响本AMF的功能可用性。

**适用NF：AMF**

该命令用于删除AMF实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFINSTANCENAME | AMF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于在UNC系统中唯一指定某个AMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。可输入的字符有字母、十进制数字、"_"和“-”，例如，AMF_Instance_0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFINFO]] · AMF信息（AMFINFO）

## 使用实例

删除当前配置的某AMF，其实例名称为AMF_Instance_0：

```
RMV AMFINFO: AMFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF信息（RMV-AMFINFO）_09653047.md`
