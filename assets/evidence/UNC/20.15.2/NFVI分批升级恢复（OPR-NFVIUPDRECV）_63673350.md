# NFVI分批升级恢复（OPR NFVIUPDRECV）

- [命令功能](#ZH-CN_MMLREF_0263673350__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0263673350__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0263673350__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0263673350__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0263673350)

该命令用于NFVI分批升级过程失败恢复。

## [注意事项](#ZH-CN_MMLREF_0263673350)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0263673350)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0263673350)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPER_MODE | 操作模式 | 可选必选说明：可选参数<br>参数含义：操作模式类型。<br>数据来源：本端规划<br>取值范围：<br>- Recovery（升级正常结束恢复）<br>- ForceRecovery（系统异常强制恢复）<br>默认值：Recovery<br>配置原则：无 |
| POD_NAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0263673350)

- NFVI分批升级恢复。
  ```
  %%OPR NFVIUPDRECV: OPER_MODE=Recovery;%%
  ```
- NFVI分批升级强制恢复。
  ```
  %%OPR NFVIUPDRECV: OPER_MODE=ForceRecovery;%%
  ```
