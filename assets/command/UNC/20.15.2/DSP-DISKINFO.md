---
id: UNC@20.15.2@MMLCommand@DSP DISKINFO
type: MMLCommand
name: DSP DISKINFO（显示节点磁盘部署规格）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DISKINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP DISKINFO（显示节点磁盘部署规格）

## 功能

该命令用于查询节点磁盘部署规格。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅在虚机场景下支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DISKINFO]] · 节点磁盘部署规格（DISKINFO）

## 使用实例

查询所有节点的磁盘部署规格。

```
%%DSP DISKINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
节点类型    节点名称     磁盘资源总量（MB）

SGU_A       10.0.0.0     31372.41
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DISKINFO.md`
