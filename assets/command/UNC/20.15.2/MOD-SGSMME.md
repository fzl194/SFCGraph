---
id: UNC@20.15.2@MMLCommand@MOD SGSMME
type: MMLCommand
name: MOD SGSMME（修改SGS MME实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSMME
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS MME实体
status: active
---

# MOD SGSMME（修改SGS MME实体）

## 功能

**适用NF：SMSF**

该命令用于修改SGS MME实体配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：0～1999。<br>默认值：无 |
| MMEM | MME名称 | 可选必选说明：可选参数<br>参数含义：该参数于用于指定与本局对接的MME的地址，MME号码长度为12位，编码格式为：MCC＋MNC＋MMEGI＋MMEC，例如，一个典型的MME号码为：“460008000101”。<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度12位。<br>默认值：无 |
| POOLGRPID | MME POOL标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME归属的MME POOL群组，该参数只有在MME为POOL组网时有效。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无 |
| MMECAPACITY | MME容量权重 | 可选必选说明：可选参数<br>参数含义：用于指定MME在所属POOL群组中的容量权重。<br>数据来源：本端规划<br>取值范围：0～100<br>默认值：无<br>说明：- 本参数功能暂未实现，因此会轮选MME POOL群组中的MME。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSMME]] · SGS MME实体（SGSMME）

## 使用实例

修改SGS MME实体，MME索引为1，MME名称为“460008000101”，MME POOL标识为1：

```
MOD SGSMME: MMEX=1, MMEM="460008000101", POOLGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SGSMME.md`
