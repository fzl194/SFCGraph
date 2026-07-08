---
id: UNC@20.15.2@MMLCommand@ADD LOCBINDAREA
type: MMLCommand
name: ADD LOCBINDAREA（增加UPF位置信息与该UPF优先支持的服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCBINDAREA
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 位置区域绑定本地优选名称
status: active
---

# ADD LOCBINDAREA（增加UPF位置信息与该UPF优先支持的服务区的绑定关系）

## 功能

**适用NF：SMF、SGW-C、GGSN、PGW-C**

该命令用于增加UPF位置信息与该UPF优先支持的服务区的绑定关系。

该命令配合ADD PNFSMFSERAREA使用，用于基于用户位置区信息选择UPF。ADD PNFSMFSERAREA配置了对端UPF为SMF提供的服务区域信息。一个UPF可能为SMF提供多个服务区域。

在用户激活时，SMF从激活请求中获取用户位置信息，从而获取用户所属的位置区名称。来自该位置区的用户可以优先匹配绑定服务区域的UPF，以获得更好的服务。

## 注意事项

- 使用命令SET UPSELECTFLAG将LOCALITY开关置为ENABLE时生效。

- 最多可输入8192条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~150。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF优先支持的服务区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。该参数取值应与配置PNFSMFSERAREA中的SmfServingArea保持一致，可通过LST PNFSMFSERAREA命令查询。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPAREA中事先配置，可执行LST UPAREA进行查看。注意查询结果中“UPF服务区名称”须包含要绑定的“UPF服务区名称”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCBINDAREA]] · UPF位置信息与该UPF优先支持的服务区的绑定关系（LOCBINDAREA）

## 使用实例

新增一组UPF位置信息与该UPF优先支持的服务区的绑定关系，其中UPF位置区为“locality1”，绑定的覆盖区域名称为“area1”：

```
ADD LOCBINDAREA: LOCALITY="locality1",AREANAME="area1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LOCBINDAREA.md`
