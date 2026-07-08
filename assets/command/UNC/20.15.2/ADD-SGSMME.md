---
id: UNC@20.15.2@MMLCommand@ADD SGSMME
type: MMLCommand
name: ADD SGSMME（增加SGS MME实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SGSMME
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
max_records: 2000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS MME实体
status: active
---

# ADD SGSMME（增加SGS MME实体）

## 功能

**适用NF：SMSF**

该命令用于增加SGS MME实体配置。

## 注意事项

- 此命令的最大记录数为2000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：0～1999。<br>默认值：无<br>配置原则：增加索引时从小到大配置。 |
| MMEM | MME名称 | 可选必选说明：必选参数<br>参数含义：该参数于用于指定与本局对接的MME的地址，MME号码长度为12位，编码格式为：MCC＋MNC＋MMEGI＋MMEC，例如，一个典型的MME号码为：“460008000101”<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度为12位。<br>默认值：无<br>配置原则：<br>- MCC（Mobile Country Code）：移动国家码，用于标识MME所属的国家。移动国家码由3位数字组成，它由ETSI在全球范围内统一分配，例如，中国的“移动国家码”为“460”、英国的“移动国家码”为“234”等。<br>- MNC（Mobile Network Code）：移动网络码，用于标识MME的归属PLMN。移动网络码由2位或3位数字组成，如果为2位的场景需要补0，它由本国电信主管部门在本国范围内统一分配，例如，目前在中国，补0后中国移动GSM网络的“移动网络码”为“000”、中国联通GSM网络的“移动网络码”为“001”等。<br>- MMEGI（MME Group ID）：MME分组内的组号，用来标识MME属于哪个POOL区。由4位字符（0～9、A～F或a～f）组成。<br>- MMEC（MME Code）：组内的MME编码，用来标识MME在POOL区内的编码。由2位字符（0～9、A～F或a～f）组成。<br>- 该参数区分大小写。 |
| POOLGRPID | MME POOL标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME归属的MME POOL群组，该参数只有在MME为POOL组网时有效。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：255<br>配置原则：无 |
| MMECAPACITY | MME容量权重 | 可选必选说明：可选参数<br>参数含义：用于指定MME在所属POOL群组中的容量权重。<br>数据来源：本端规划<br>取值范围：0～100<br>默认值：100<br>配置原则：无<br>说明：- 本参数功能暂未实现，因此会轮选MME POOL群组中的MME。 |

## 操作的配置对象

- [SGS MME实体（SGSMME）](configobject/UNC/20.15.2/SGSMME.md)

## 使用实例

增加SGS MME实体，MME索引为1，MME名称为“460008000101”，MME POOL标识为1：

```
ADD SGSMME: MMEX=1, MMEM="460008000101", POOLGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SGS-MME实体(ADD-SGSMME)_93164005.md`
