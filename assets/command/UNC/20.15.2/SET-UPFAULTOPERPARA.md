---
id: UNC@20.15.2@MMLCommand@SET UPFAULTOPERPARA
type: MMLCommand
name: SET UPFAULTOPERPARA（设置UP故障处理系统参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPFAULTOPERPARA
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 辅锚点故障迁移
status: active
---

# SET UPFAULTOPERPARA（设置UP故障处理系统参数）

## 功能

**适用NF：SMF**

该命令用于设置UP故障处理的系统参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UPMIGRATE |
| --- |
| 1000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPMIGRATE | 故障迁移速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于控制副锚点UPF故障时，系统批量迁移或者批量删除分流业务的速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~5000。单位个/秒，向上取整。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPFAULTOPERPARA查询当前参数配置值。<br>配置原则：<br>副锚点UPF的APSAMIGFUNC=ENABLE，该参数控制系统批量迁移分流业务的速率。<br>副锚点UPF的APSAMIGFUNC=DISABLE，该参数控制系统批量删除分流业务的速率。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFAULTOPERPARA]] · UP故障处理系统参数（UPFAULTOPERPARA）

## 使用实例

设置副锚点UPF故障时，系统批量迁移副锚点UPF上会话的速率是1000个/秒：

```
SET UPFAULTOPERPARA: UPMIGRATE=1000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-UPFAULTOPERPARA.md`
