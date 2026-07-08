---
id: UNC@20.15.2@MMLCommand@MOD SGSRLKS
type: MMLCommand
name: MOD SGSRLKS（修改SGS服务端链路集）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSRLKS
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
- SGS服务端链路集
status: active
---

# MOD SGSRLKS（修改SGS服务端链路集）

## 功能

**适用NF：SMSF**

此命令用于修改SGS服务端链路集配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~2000<br>默认值：无 |
| MMEN | MME索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端MME提供的索引号。<br>数据来源：整网规划<br>取值范围：0~1999<br>默认值：无<br>配置原则：须先在<br>[ADD SGSMME](../SGS MME实体/增加SGS MME实体(ADD SGSMME)_93164005.md)<br>中配置取值相同的<br>“MMEX”<br>参数。 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数说明：该参数用于指定链路集的名称。<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度范围为0~255<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSRLKS]] · SGS服务端链路集（SGSRLKS）

## 使用实例

1. 修改链路集索引为0的SGS服务端链路集配置，可以用如下命令：
  ```
  MOD SGSRLKS: LSX=0, LSN="huawei";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SGSRLKS.md`
