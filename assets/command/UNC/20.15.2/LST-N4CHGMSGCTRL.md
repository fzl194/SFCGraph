---
id: UNC@20.15.2@MMLCommand@LST N4CHGMSGCTRL
type: MMLCommand
name: LST N4CHGMSGCTRL（查询N4接口计费消息相关控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N4CHGMSGCTRL
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST N4CHGMSGCTRL（查询N4接口计费消息相关控制参数）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询N4接口计费消息相关控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N4CHGMSGCTRL]] · N4接口计费消息相关控制参数（N4CHGMSGCTRL）

## 使用实例

查询N4接口计费消息相关控制参数：

```
%%LST N4CHGMSGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                     消息缓存池扩展开关  =  使能
                         缓存池满的动作  =  去活PDU会话
 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N4CHGMSGCTRL.md`
