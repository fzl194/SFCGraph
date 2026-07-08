---
id: UNC@20.15.2@MMLCommand@DSP LCSBYIMSI
type: MMLCommand
name: DSP LCSBYIMSI（显示指定IMSI用户LCS签约信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LCSBYIMSI
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP LCSBYIMSI（显示指定IMSI用户LCS签约信息）

## 功能

**适用网元：SGSN、MME**

该命令用于根据IMSI查询LCS签约数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>取值范围：0～15位数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCSBYIMSI]] · 指定IMSI用户LCS签约信息（LCSBYIMSI）

## 使用实例

查询当前系统中IMSI为“123031500000002”的用户的LCS签约数据信息：

DSP LCSBYIMSI: IMSI="123031500000002";

```
%%DSP LCSBYIMSI: IMSI="123031500000002";%%
RETCODE = 0  操作成功。

GMLC列表
---------
        GMLC1  =  8613915801
        GMLC2  =  NULL
        GMLC3  =  NULL
        GMLC4  =  NULL
        GMLC5  =  NULL
仍有后续报告输出
---    END

%%DSP LCSBYIMSI: IMSI="123031500000002";%%
RETCODE = 0  操作成功。

GMLC列表
---------
                                 索引   =  1
                 LCS隐私类补充业务编码  =  通用
                 LCS隐私类补充业务状态  =  0500000000
        非列表客户端的定位隐私权限标志  =  NULL
            非列表客户端的定位隐私权限  =  NULL
                    外部客户端地址长度  =  NULL
                        外部客户端地址  =  NULL
                          GMLC限制标志  =  NULL
                              GMLC限制  =  NULL
          列表客户端的定位隐私权限标志  =  NULL
              列表客户端的定位隐私权限  =  NULL
                        PLMN客户端列表  =  FFFFFFFFFF
仍有后续报告输出
---    END

%%DSP LCSBYIMSI: IMSI="123031500000002";%%
RETCODE = 0  操作成功。

GMLC列表
---------
 MOLR类补充业务编码  MOLR类补充业务状态
 所有MOLR类          0500000000
  NULL               0000000000
  NULL               0000000000
(结果个数 = 5)
共3个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LCSBYIMSI.md`
