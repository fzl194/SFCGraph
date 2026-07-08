---
id: UNC@20.15.2@MMLCommand@LST SECDEVURPF
type: MMLCommand
name: LST SECDEVURPF（查询设备URPF）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECDEVURPF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略设备URPF
status: active
---

# LST SECDEVURPF（查询设备URPF）

## 功能

该命令用来查询安全策略URPF配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECDEVURPF]] · 设备URPF（SECDEVURPF）

## 使用实例

查询安全策略中的URPF配置：

```
LST SECDEVURPF:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
        策略编号  =  1
安全URPF检查类型  =  严格检查
是否允许缺省路由  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SECDEVURPF.md`
