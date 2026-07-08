---
id: UNC@20.15.2@MMLCommand@DSP RDSAUTHLINKINFO
type: MMLCommand
name: DSP RDSAUTHLINKINFO（显示Radius鉴权路径信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RDSAUTHLINKINFO
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- Radius鉴权链路状态
status: active
---

# DSP RDSAUTHLINKINFO（显示Radius鉴权路径信息）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查看Radius鉴权路径信息。当前最多支持显示100条历史链路。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSAUTHLINKINFO]] · Radius鉴权路径信息（RDSAUTHLINKINFO）

## 使用实例

显示Radius鉴权路径信息。

```
%%DSP RDSAUTHLINKINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
本端IPv4地址        对端IPv4地址       本端IPv6地址        对端IPv6地址       VPN实例       路径状态变更       变更时间戳     

10.2.3.4             10.70.18.56        ::                  ::                 _public_      UP->DOWN           2021-06-21 08:04:48
10.2.3.4             10.70.18.40        ::                  ::                 _public_      UP->DOWN           2021-06-21 08:04:48
10.2.3.4             10.70.18.42        ::                  ::                 _public_      UP->DOWN           2021-06-21 08:04:48
10.2.3.4             10.70.18.56        ::                  ::                 _public_      DOWN->UP           2021-06-21 08:05:16
10.2.3.4             10.70.18.40        ::                  ::                 _public_      DOWN->UP           2021-06-21 08:05:16
10.2.3.4             10.70.18.42        ::                  ::                 _public_      DOWN->UP           2021-06-21 08:05:16
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RDSAUTHLINKINFO.md`
