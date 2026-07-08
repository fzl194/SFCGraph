---
id: UNC@20.15.2@MMLCommand@RMV LOCBINDS1TAI
type: MMLCommand
name: RMV LOCBINDS1TAI（删除UPF位置信息与UPF优先支持的4G TAI范围的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCBINDS1TAI
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 位置区域绑定4G TAI范围
status: active
---

# RMV LOCBINDS1TAI（删除UPF位置信息与UPF优先支持的4G TAI范围的绑定关系）

## 功能

**适用NF：SGW-C**

该命令用于删除UPF位置信息与UPF优先支持的TAI范围的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |
| S1TACSTART | S1 TAC起始号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC的起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是4。不区分大小写。<br>默认值：无<br>配置原则：<br>字符串类型，4位16进制数。<br>TAC的终止号段需要不小于TAC的起始号段，且结束值和开始值长度需相等。 |
| S1TACEND | S1 TAC终止号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC的终止号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是4。不区分大小写。<br>默认值：无<br>配置原则：<br>字符串类型，4位16进制数。<br>TAC的终止号段需要不小于TAC的起始号段，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [UPF位置信息与UPF优先支持的4G TAI范围的绑定关系（LOCBINDS1TAI）](configobject/UNC/20.15.2/LOCBINDS1TAI.md)

## 使用实例

删除UPF位置区与UPF优先支持的TAI范围的绑定关系，其中UPF位置区为“locality1”，MCC为460, MNC为03，S1 TAC起始号段为1301，S1 TAC终止号段为1302。

```
RMV LOCBINDS1TAI: LOCALITY="locality1",MCC="460",MNC="03",S1TACSTART="1301",S1TACEND="1302";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF位置信息与UPF优先支持的4G-TAI范围的绑定关系（RMV-LOCBINDS1TAI）_96242800.md`
