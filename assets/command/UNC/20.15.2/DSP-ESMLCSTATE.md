---
id: UNC@20.15.2@MMLCommand@DSP ESMLCSTATE
type: MMLCommand
name: DSP ESMLCSTATE（显示ESMLC状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ESMLCSTATE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS操作维护
status: active
---

# DSP ESMLCSTATE（显示ESMLC状态）

## 功能

**适用网元：MME**

此命令用于查询指定ESMLC设备状态，以及MME与ESMLC之间的所有链路状态。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESMLCID | E-SMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的E-SMLC 标识，E-SMLC 标识可以通过<br>[**LST LCSAPLNK**](../LCSAP链路配置/查询LCSAP链路配置(LST LCSAPLNK)_26305618.md)<br>命令查询。<br>取值范围：0～255<br>默认值 ：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ESMLCSTATE]] · ESMLC状态（ESMLCSTATE）

## 使用实例

查询 “E-SMLC 标识” 为 “3” 的ESMLC状态

DSP ESMLCSTATE: ESMLCID=3;

```
%%DSP ESMLCSTATE: ESMLCID=3;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
      E-SMLC 标识  =  3
      E-SMLC 状态  =  稳态
    E-SMLC 优先级  =  3
E-SMLC 定位用户数  =  30
           链路数  =  3
仍有后续报告输出
---    END

%%DSP ESMLCSTATE: ESMLCID=3;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
链路索引            RU名称            进程号      链路状态

5                   USN_SP_RU_0064    0           稳态
11                  USN_SP_RU_0065    1           无效
17                  USN_SP_RU_0064    0           稳态
(结果个数 = 4)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ESMLCSTATE.md`
