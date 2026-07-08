---
id: UNC@20.15.2@MMLCommand@CLR DYNNRFSTAT
type: MMLCommand
name: CLR DYNNRFSTAT（清除内部统计信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: DYNNRFSTAT
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# CLR DYNNRFSTAT（清除内部统计信息）

## 功能

**适用NF：NRF**

清除NRF内部统计信息。清除之前的NF访问信息，内存中记录从当前开始的NF访问信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DYNNRFSTAT]] · 内部统计信息（DYNNRFSTAT）

## 使用实例

将内部统计项清零：

```
CLR DYNNRFSTAT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-DYNNRFSTAT.md`
