---
id: UNC@20.15.2@MMLCommand@LST IMSDDNFLOWCTRLCHR
type: MMLCommand
name: LST IMSDDNFLOWCTRLCHR（查询IMS DDN流量控制上报CHR配置开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSDDNFLOWCTRLCHR
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- IMS DDN流量控制上报CHR配置
status: active
---

# LST IMSDDNFLOWCTRLCHR（查询IMS DDN流量控制上报CHR配置开关）

## 功能

**适用NF：SGW-C**

该命令用来查看语音IMS的DDN消息流控时是否上报CHR功能的开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSDDNFLOWCTRLCHR]] · IMS DDN流量控制上报CHR配置开关（IMSDDNFLOWCTRLCHR）

## 使用实例

显示语音IMS的DDN消息流控时上报CHR功能开关状态：

```
%%LST IMSDDNFLOWCTRLCHR:;%%
RETCODE = 0  操作成功

结果如下
--------
IMS DDN流量控制上报CHR配置开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSDDNFLOWCTRLCHR.md`
