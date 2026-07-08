---
id: UDG@20.15.2@MMLCommand@SET VOLTEMOSFACTOR
type: MMLCommand
name: SET VOLTEMOSFACTOR（设置MOS计算值的补偿因子）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VOLTEMOSFACTOR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE MOS 补充因子
status: active
---

# SET VOLTEMOSFACTOR（设置MOS计算值的补偿因子）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置MOS计算值的补偿因子。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10。
- 如果MOSCODEC设置为MOS_CODEC_ALL，则表示对所有MOSCODEC进行设置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MOSCODEC | FACTOR0TO1 | FACTOR1TO2 | FACTOR2TO3 | FACTOR3TO4 | FACTOR4TO5 |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | MOS_CODEC_AMR_NB | 0 | 0 | 0 | 0 | 0 |
| 初始值 | MOS_CODEC_AMR_WB | 0 | 0 | 0 | 0 | 0 |
| 初始值 | MOS_CODEC_G711 | 0 | 0 | 0 | 0 | 0 |
| 初始值 | MOS_CODEC_G722 | 0 | 0 | 0 | 0 | 0 |
| 初始值 | MOS_CODEC_G729 | 0 | 0 | 0 | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSCODEC | 语音编解码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指语音编解码类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MOS_CODEC_AMR_NB：编解码类型为AMR NB。<br>- MOS_CODEC_AMR_WB：编解码类型为AMR WB。<br>- MOS_CODEC_G711：编解码类型为G.711。<br>- MOS_CODEC_G722：编解码类型为G.722。<br>- MOS_CODEC_G729：编解码类型为G.729。<br>- MOS_CODEC_EVS_NB：编解码类型为EVS NB。<br>- MOS_CODEC_EVS_WB：编解码类型为EVS WB。<br>- MOS_CODEC_EVS_SWB：编解码类型为EVS SWB。<br>- MOS_CODEC_EVS_FB：编解码类型为EVS FB。<br>- MOS_CODEC_EVS_AMR：编解码类型为EVS AMR-WB IO。<br>- MOS_CODEC_ALL：支持的全部语音编解码类型。<br>默认值：无<br>配置原则：无 |
| FACTOR0TO1 | MOS补偿因子1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定丢包率小于1%时的MOS补偿因子。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。输入必须为-10~10的字符串形式，粒度为100。<br>默认值：无<br>配置原则：无 |
| FACTOR1TO2 | MOS补偿因子2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定丢包率大于等于1%并且小于2%时的MOS补偿因子。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。输入必须为-10~10的字符串形式，粒度为100。<br>默认值：无<br>配置原则：无 |
| FACTOR2TO3 | MOS补偿因子3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定丢包率大于等于2%并且小于3%时的MOS补偿因子。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。输入必须为-10~10的字符串形式，粒度为100。<br>默认值：无<br>配置原则：无 |
| FACTOR3TO4 | MOS补偿因子4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定丢包率大于等于3%并且小于4%时的MOS补偿因子。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。输入必须为-10~10的字符串形式，粒度为100。<br>默认值：无<br>配置原则：无 |
| FACTOR4TO5 | MOS补偿因子5 | 可选必选说明：可选参数<br>参数含义：该参数用于指定丢包率大于等于4%并且小于5%时的MOS补偿因子。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。输入必须为-10~10的字符串形式，粒度为100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [MOS补偿因子（VOLTEMOSFACTOR）](configobject/UDG/20.15.2/VOLTEMOSFACTOR.md)

## 使用实例

- 设置AMR WB编解码语音的MOS计算值的补偿因子：
  ```
  SET VOLTEMOSFACTOR: MOSCODEC=MOS_CODEC_AMR_WB, FACTOR1TO2="1", FACTOR2TO3="-1";
  ```
- 设置所有编解码语音的MOS计算值的补偿因子：
  ```
  SET VOLTEMOSFACTOR: MOSCODEC=MOS_CODEC_ALL, FACTOR1TO2="1", FACTOR2TO3="-1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置MOS计算值的补偿因子（SET-VOLTEMOSFACTOR）_57538685.md`
