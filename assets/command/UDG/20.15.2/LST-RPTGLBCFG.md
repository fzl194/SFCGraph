---
id: UDG@20.15.2@MMLCommand@LST RPTGLBCFG
type: MMLCommand
name: LST RPTGLBCFG（查询业务报表全局开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTGLBCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表全局开关
status: active
---

# LST RPTGLBCFG（查询业务报表全局开关）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询业务报表全局开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RPTGLBCFG]] · 业务报表全局开关（RPTGLBCFG）

## 使用实例

假如运营商需要查询业务报表开关：

```
LST RPTGLBCFG:;
```

```

RETCODE = 0  操作成功

业务报表全局开关配置信息
------------------------
                     全局业务报表上报开关  =  不使能（关闭）
                      TCP业务分析上报开关  =  不使能（关闭）
                      UDP业务分析上报开关  =  不使能（关闭）
                      DNS业务分析上报开关  =  不使能（关闭）
                             订阅策略开关  =  不使能（关闭）
                             配置策略开关  =  不使能（关闭）
                                 缓存开关  =  不使能（关闭）
       用户更新消息触发UFDR_FlowStats开关  =  不使能（关闭）
对端设备信令地址更新触发UFDR_UserInfo开关  =  不使能（关闭）
                              SIP上报开关  =  不使能（关闭）
                VoLTE语音质量分析上报开关  =  不使能（关闭）
                 VoNR语音质量分析上报开关  =  不使能（关闭）
           用户组级带宽控制器信息上报开关  =  不使能（关闭）
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTGLBCFG.md`
