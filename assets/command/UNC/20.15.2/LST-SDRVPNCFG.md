---
id: UNC@20.15.2@MMLCommand@LST SDRVPNCFG
type: MMLCommand
name: LST SDRVPNCFG（查询SDR VPN配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDRVPNCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# LST SDRVPNCFG（查询SDR VPN配置信息）

## 功能

查询SDR写在ACS数据库的VPN配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRVPNCFG]] · SDR VPN配置信息（SDRVPNCFG）

## 使用实例

使用如下命令查询SDR VPN配置信息：

```
%%LST SDRVPNCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
VPN名  =  vpna
VPN索引  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SDRVPNCFG.md`
