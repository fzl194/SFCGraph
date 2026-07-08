---
id: UNC@20.15.2@MMLCommand@RMV POOLLA
type: MMLCommand
name: RMV POOLLA（删除POOL LA配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: POOLLA
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL LA配置
status: active
---

# RMV POOLLA（删除POOL LA配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于删除Pool区域LAC值，或TAI与LAC的对应关系。

## 注意事项

- 此命令执行后立即生效。
- 当表中的所有记录都没有配置“起始TAI”和“终止TAI”时，该命令删除的是Pool区域的LAC值。
- 当表中的所有记录都配置了“起始TAI”和“终止TAI”时，该命令删除的是TAI与LAC的对应关系。
- 删除Pool区域的LAC值，MME给eNodeB下发的Mapping GUMMEI中，MMEGI字段将不包含删除的记录中配置的LAC；如果删除了最后一条POOL LA记录，则给eNodeB下发的Mapping GUMMEI中包含的是MMEID中配置的MMEGI。删除TAI与LAC的对应关系后，MME给此TA覆盖的eNodeB下发Mapping GUMMEI时，MMEGI字段将不包含此记录中配置的LAC；如果删除的是TA对应的最后一条POOL LA记录时，则给此TA覆盖的eNodeB下发Mapping GUMMEI中包含的是MMEID中配置的MMEGI。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGNTAI | 起始TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>取值范围：9～10位的十六进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>取值范围：4位的十六进制数字<br>默认值：无<br>说明：- “起始TAI”和“位置区域码”至少要输入一个。<br>- 如果只输入“位置区域码”，该命令会删除所有与此LAC对应的记录。 |

## 操作的配置对象

- [POOL LA配置信息（POOLLA）](configobject/UNC/20.15.2/POOLLA.md)

## 使用实例

删除起始TAI号为"308011033"的TAI区间与LAC对应关系：

RMV POOLLA: BGNTAI="308011033";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除POOL-LA配置信息（RMV-POOLLA）_26305914.md`
