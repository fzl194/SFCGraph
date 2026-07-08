# 查询NSEI和BSSID值的对应关系(LST BSSIDFORNSEI)

- [命令功能](#ZH-CN_MMLREF_0000001126305806__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305806__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305806__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305806__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305806__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305806__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305806__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305806)

**适用网元：SGSN**

此命令用于查询NSEI和BSSID值的对应关系。只适用于Gb over IP自动配置的场景。

#### [注意事项](#ZH-CN_MMLREF_0000001126305806)

- 此命令执行后立即生效。
- 当一组NSE与BSSID值的对应关系“BSSIDRULE”不是“NSEI_MAP_SPECIFIC_BSSID(指定BSSID)”时，“BSS标识”显示为NULL。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305806)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305806)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305806)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | 起始NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询NSEI和BSSID值对应关系的网络服务实体起始标识。<br>取值范围：0～65535<br>默认值：无<br>说明：本参数为<br>[**ADD BSSIDFORNSEI**](增加NSEI和BSSID值的对应关系(ADD BSSIDFORNSEI)_72345595.md)<br>中存在的起始NSE标识。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305806)

1. 查询所有NSEI和BSSID值的对应关系：
  LST BSSIDFORNSEI:;
  ```
  LST BSSIDFORNSEI:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  起始NSE标识  结束NSE标识   BSSID与NSEI的对应关系  BSS标识
  0            5             指定BSSID              2
  7            8             NSEI去掉前3位          NULL
  (结果个数 = 2)

  ---    END
  ```
2. 查询 “ 起始NSE标识 ” 为 “0” 的记录：
  LST BSSIDFORNSEI: NSEI=0;
  ```
  %%LST BSSIDFORNSEI: NSEI=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
            起始NSE标识  =  0
            结束NSE标识  =  5
  BSSID与NSEI的对应关系  =  指定BSSID
                BSS标识  =  2
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305806)

参见 [**ADD BSSIDFORNSEI**](增加NSEI和BSSID值的对应关系(ADD BSSIDFORNSEI)_72345595.md) 的参数说明。
