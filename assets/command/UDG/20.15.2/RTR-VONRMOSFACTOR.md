---
id: UDG@20.15.2@MMLCommand@RTR VONRMOSFACTOR
type: MMLCommand
name: RTR VONRMOSFACTOR（恢复MOS补偿因子）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VONRMOSFACTOR
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS 补充因子
status: active
---

# RTR VONRMOSFACTOR（恢复MOS补偿因子）

## 功能

**适用NF：UPF**

该命令用于恢复MOS补偿因子为系统初始设置值。

## 注意事项

- 该命令执行后立即生效。
- 如果MOSCODEC设置为SM_MOS_CODEC_ALL，则表示对所有MOSCODEC进行设置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSCODEC | 语音编解码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指语音编解码类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MOS_CODEC_AMR_NB：编解码类型为AMR NB。<br>- MOS_CODEC_AMR_WB：编解码类型为AMR WB。<br>- MOS_CODEC_G711：编解码类型为G.711。<br>- MOS_CODEC_G722：编解码类型为G.722。<br>- MOS_CODEC_G729：编解码类型为G.729。<br>- MOS_CODEC_EVS_NB：编解码类型为EVS NB。<br>- MOS_CODEC_EVS_WB：编解码类型为EVS WB。<br>- MOS_CODEC_EVS_SWB：编解码类型为EVS SWB。<br>- MOS_CODEC_EVS_FB：编解码类型为EVS FB。<br>- MOS_CODEC_EVS_AMR：编解码类型为EVS AMR-WB IO。<br>- MOS_CODEC_ALL：支持的全部语音编解码类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VONRMOSFACTOR]] · MOS补偿因子（VONRMOSFACTOR）

## 使用实例

- 恢复AMR WB编解码语音的MOS计算值的补偿因子为系统初始设置值：
  ```
  RTR VONRMOSFACTOR: MOSCODEC=MOS_CODEC_AMR_WB;
  ```
- 恢复所有编解码语音的MOS补偿因子为系统初始设置值，初始值见SET VONRMOSFACTOR：
  ```
  RTR VONRMOSFACTOR: MOSCODEC=MOS_CODEC_ALL;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-VONRMOSFACTOR.md`
