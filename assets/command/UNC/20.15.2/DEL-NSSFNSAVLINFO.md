---
id: UNC@20.15.2@MMLCommand@DEL NSSFNSAVLINFO
type: MMLCommand
name: DEL NSSFNSAVLINFO（删除切片可用性信息）
nf: UNC
version: 20.15.2
verb: DEL
object_keyword: NSSFNSAVLINFO
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DEL NSSFNSAVLINFO（删除切片可用性信息）

## 功能

![](删除切片可用性信息（DEL NSSFNSAVLINFO）_96241943.assets/notice_3.0-zh-cn_2.png)

此命令用于在NSSF上强制删除指定AMF的切片可用性信息，会导致AMF已上报的该切片数据不可用，删除之前请联系华为技术工程师进行风险评估。

**适用NF：NSSF**

该命令用于将AMF已上报的切片可用性信息删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFINSTANCEID | AMF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示AMF实例标识，此命令会删除该标识指定的AMF上报的可用性信息，该参数可以根据DSP NSSFNSAVLINFO查询获得。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFNSAVLINFO]] · 切片可用性信息（NSSFNSAVLINFO）

## 使用实例

删除ID为123e4567-e89b-12d3-a456-42665544cced的AMF对应的切片可用性信息：

```
DEL NSSFNSAVLINFO: AMFINSTANCEID="123e4567-e89b-12d3-a456-42665544cced";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除切片可用性信息（DEL-NSSFNSAVLINFO）_96241943.md`
