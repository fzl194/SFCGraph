# 恢复MOS补偿因子（RTR VONRMOSFACTOR）

- [命令功能](#ZH-CN_CONCEPT_0000203181894388__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203181894388__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203181894388__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203181894388__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203181894388__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203181894388)

**适用NF：UPF**

该命令用于恢复MOS补偿因子为系统初始设置值。

#### [注意事项](#ZH-CN_CONCEPT_0000203181894388)

- 该命令执行后立即生效。
- 如果MOSCODEC设置为SM_MOS_CODEC_ALL，则表示对所有MOSCODEC进行设置。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203181894388)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203181894388)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSCODEC | 语音编解码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指语音编解码类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MOS_CODEC_AMR_NB：编解码类型为AMR NB。<br>- MOS_CODEC_AMR_WB：编解码类型为AMR WB。<br>- MOS_CODEC_G711：编解码类型为G.711。<br>- MOS_CODEC_G722：编解码类型为G.722。<br>- MOS_CODEC_G729：编解码类型为G.729。<br>- MOS_CODEC_EVS_NB：编解码类型为EVS NB。<br>- MOS_CODEC_EVS_WB：编解码类型为EVS WB。<br>- MOS_CODEC_EVS_SWB：编解码类型为EVS SWB。<br>- MOS_CODEC_EVS_FB：编解码类型为EVS FB。<br>- MOS_CODEC_EVS_AMR：编解码类型为EVS AMR-WB IO。<br>- MOS_CODEC_ALL：支持的全部语音编解码类型。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203181894388)

- 恢复AMR WB编解码语音的MOS计算值的补偿因子为系统初始设置值：
  ```
  RTR VONRMOSFACTOR: MOSCODEC=MOS_CODEC_AMR_WB;
  ```
- 恢复所有编解码语音的MOS补偿因子为系统初始设置值，初始值见SET VONRMOSFACTOR：
  ```
  RTR VONRMOSFACTOR: MOSCODEC=MOS_CODEC_ALL;
  ```
