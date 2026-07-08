# 恢复Tethering用户终端数量检测全局配置（RTR TETHERDETGLBPARA）

- [命令功能](#ZH-CN_CONCEPT_0182837445__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837445__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837445__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837445__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837445__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837445)

**适用NF：PGW-U、UPF**

该命令用来恢复Tethering用户终端数量检测全局配置为初始值。

#### [注意事项](#ZH-CN_CONCEPT_0182837445)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837445)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837445)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 需要删除的Tethering用户终端数量检测全局配置参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要删除的Tethering用户终端数量检测全局配置参数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AGE_TIME：恢复 AGE_TIME的初始值。<br>- HOTSPOT_AGE_TIME_PARA：恢复HOTSPOT_AGE_TIME_PARA的初始值。<br>- TTL_ANTI_FRAUD：恢复TTL_ANTI_FRAUD的初始值。<br>- PCC_MAX_NUM_CHOICE：恢复PCC_MAX_NUM_CHOICE的初始值。<br>- BWM_SUBSCRIBE_CONTROLLER：恢复BWM_SUBSCRIBE_CONTROLLER的初始值。<br>- STATISTIC_METHOD：恢复STATISTIC_METHOD的初始值。<br>- UDP_CONTROL_MODE：恢复UDP_CONTROL_MODE的初始值。<br>默认值：无<br>配置原则：如果未指定RMVTYPE，则恢复所有Tethering用户终端数量检测全局配置参数的初始值。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837445)

恢复Tethering用户终端数量检测全局配置，使用此命令：

```
RTR TETHERDETGLBPARA:;
```
