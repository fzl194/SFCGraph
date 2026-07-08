---
id: UNC@20.15.2@MMLCommand@LST DFTPROXYCTRL
type: MMLCommand
name: LST DFTPROXYCTRL（查询缺省代理控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTPROXYCTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- 缺省代理控制
status: active
---

# LST DFTPROXYCTRL（查询缺省代理控制配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询缺省代理控制配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DFTPROXYCTRL]] · 缺省代理控制配置（DFTPROXYCTRL）

## 使用实例

查询缺省的代理控制配置：

```
%%LST DFTPROXYCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
支持语音业务回归属地功能开关  =  关闭
                         归属地接口模式  =   与左侧联动
       数据业务回归属地功能开关  =    关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DFTPROXYCTRL.md`
