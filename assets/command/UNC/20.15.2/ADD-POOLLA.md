---
id: UNC@20.15.2@MMLCommand@ADD POOLLA
type: MMLCommand
name: ADD POOLLA（增加POOL LA配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: POOLLA
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL LA配置
status: active
---

# ADD POOLLA（增加POOL LA配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于增加Pool区域LAC值，或TAI与LAC的对应关系。

## 注意事项

- 此命令执行后立即生效。
- 该表最大记录数为20000。但当表中的所有记录都没有配置“起始TAI”和“终止TAI”时，该表能允许添加的最大记录数为1024。
- 所有POOL LA记录或者均包含TA区间、或者均不包含TA区间，并且每条记录的TA区间所包含的TAI个数不能超过20000。
- 当表中的所有POOL LA记录都没有配置“起始TAI”和“终止TAI”时，该命令增加的是Pool区域的LAC值。
- 当表中的所有POOL LA记录都配置了“起始TAI”和“终止TAI”时，该命令增加的是TAI与LAC的对应关系。
- 融合POOL组网场景下，ADD POOL命令中输入的“NRI长度”不能大于8。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGNTAI | 起始TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>数据来源：整网规划<br>取值范围：9～10位的16进制数字<br>默认值：无<br>配置原则：<br>- 起始TAI由MCC、MNC、TAC组成。<br>- MCC为3个数字，MNC为2个或者3个数字，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位。 |
| ENDTAI | 终止TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个终止跟踪区。<br>数据来源：整网规划<br>取值范围：9～10位的16进制数字<br>默认值：无<br>配置原则：<br>- 终止TAI由MCC、MNC、TAC组成。<br>- MCC为3个数字，MNC为2个或者3个数字，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位。<br>- 如果不输入“起始TAI”，则不允许输入“终止TAI”。<br>- 输入参数“终止TAI”要大于或等于“起始TAI”。<br>- 如果未输入“终止TAI”且“起始TAI”完整则表示某个固定的“起始TAI”对应到某个LAC，即“终止TAI”等于“起始TAI”。<br>- 新增的TAI区间不能和POOLLA表中已有的TAI区间存在交集，但可以完全重叠，POOL LA表中的TAI区间完全相同的最大记录数为6。 |
| LAC | 位置区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>数据来源：整网规划<br>取值范围：4位的十六进制数字<br>默认值：无<br>配置原则：<br>- LAC编码为16进制数，固定为4位。<br>- LAC可以重复，一个LAC可对应多个TAI区间。但当表中的所有记录都没有配置TAI区间时，LAC不可以重复。<br>说明：增加Pool区域的LAC值，MME给eNodeB下发的Mapping GUMMEI中，MMEGI字段将包含增加的记录中配置的LAC；增加TAI与LAC的对应关系后，MME给此TA覆盖的eNodeB下发Mapping GUMMEI时，MMEGI字段将包含此记录中配置的LAC；如果表中没有配置POOL LA记录，则给eNodeB下发的Mapping GUMMEI中包含的是MMEID中配置的MMEGI。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POOLLA]] · POOL LA配置信息（POOLLA）

## 使用实例

1. 增加起始TAI号为“308014101”，终止TAI为“308014103”，LAC为“0001”的TAI与LAC对应关系：
  ADD POOLLA: BGNTAI="308014101", ENDTAI="308014103", LAC="0001";
2. 增加TAI号为“308015101”，LAC为“0001”的TAI与LAC对应关系：
  ADD POOLLA: BGNTAI="308015101", LAC="0001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-POOLLA.md`
