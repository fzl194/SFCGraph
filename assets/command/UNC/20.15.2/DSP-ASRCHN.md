---
id: UNC@20.15.2@MMLCommand@DSP ASRCHN
type: MMLCommand
name: DSP ASRCHN（显示容灾业务通道状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ASRCHN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 主备容灾管理
- 容灾业务通道
status: active
---

# DSP ASRCHN（显示容灾业务通道状态）

## 功能

**适用网元：SGSN、MME**

该命令已废弃。

该命令用于显示主备网元之间的容灾业务通道状态和网元的主备状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHNID | 容灾业务通道ID | 参数含义：该参数用于指定需要显示的业务容灾通道的序号。<br>取值范围：0~0<br>默认值：无。 |

## 操作的配置对象

- [容灾业务通道配置（ASRCHN）](configobject/UNC/20.15.2/ASRCHN.md)

## 使用实例

查询主备网元之间的容灾业务通道状态和网元的主备状态。

DSP ASRCHN:;

```
%%DSP ASRCHN:;%%
RETCODE = 0  执行成功

-------------------------
容灾业务通道ID   = 0
通道状态         = 正常
本端网元运行状态 = 正常
对端网元运行状态 = 正常

仍有后续报告输出...
---    END

%%DSP ASRCHN:;%%
RETCODE = 0  执行成功
-------------------------
容灾业务通道本端IP    容灾业务通道本端端口    容灾业务通道对端IP    容灾业务通道对端端口    路径状态
10.10.27.100          18100                   10.10.28.100         18100                   路径正常
10.10.27.100          18100                   10.10.28.101         18100                   路径正常
10.10.27.101          18100                   10.10.28.100         18100                   路径正常
10.10.27.101          18100                   10.10.28.101         18100                   路径正常
(结果个数 = 5)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示容灾业务通道状态(DSP-ASRCHN)_26305938.md`
