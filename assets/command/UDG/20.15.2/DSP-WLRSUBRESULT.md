---
id: UDG@20.15.2@MMLCommand@DSP WLRSUBRESULT
type: MMLCommand
name: DSP WLRSUBRESULT（显示APP订阅结果信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRSUBRESULT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示APP订阅信息
status: active
---

# DSP WLRSUBRESULT（显示APP订阅结果信息）

## 功能

该命令用于显示APP订阅结果信息。

## 注意事项

只有建立无线路由对端peer后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEER | PEER地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示PEER地址。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～64。IP地址。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@WLRSUBRESULT]] · APP订阅结果信息（WLRSUBRESULT）

## 使用实例

显示APP订阅结果信息：

```
DSP WLRSUBRESULT:;
```

```

RETCODE = 0  操作成功

结果如下
--------
VPN名字              PEER地址    TB high    TB low    TP      VPN标签    VPN通告状态    PAE状态

__mpp_vpn_inner__    10.1.1.1    0          64        4098    0          --             Normal
__mpp_vpn_inner__    10.1.1.1    0          65        4098    0          --             Abnormal
_public_             10.1.1.1    0          64        4098    1          --             Normal
_public_             10.1.1.1    0          65        4098    1          --             Abnormal
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-WLRSUBRESULT.md`
