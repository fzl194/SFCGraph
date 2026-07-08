---
id: UNC@20.15.2@MMLCommand@LST N7SNDATTRCTRL
type: MMLCommand
name: LST N7SNDATTRCTRL（查询N7发送信元处理控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N7SNDATTRCTRL
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 23G接入控制
status: active
---

# LST N7SNDATTRCTRL（查询N7发送信元处理控制）

## 功能

**适用NF：GGSN**

该命令用于查询N7接口发送消息中部分信元的处理方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N7SNDATTRCTRL]] · N7发送信元处理控制（N7SNDATTRCTRL）

## 使用实例

查询N7接口发送消息中部分信元的处理方式。

```
%%LST N7SNDATTRCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
携带GERAN类信元  =  是
携带UTRAN类信元  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N7SNDATTRCTRL.md`
