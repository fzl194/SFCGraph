---
id: UNC@20.15.2@MMLCommand@LST VLRUSRNUMCHECK
type: MMLCommand
name: LST VLRUSRNUMCHECK（查询VLR非短信用户数核查扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRUSRNUMCHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 数据核查
status: active
---

# LST VLRUSRNUMCHECK（查询VLR非短信用户数核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于查询VLR非短信用户数核查扫描参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VLRUSRNUMCHECK]] · VLR非短信用户数核查扫描参数（VLRUSRNUMCHECK）

## 使用实例

运营商希望查询VLR非短信用户数核查扫描参数，执行如下命令：

```
LST VLRUSRNUMCHECK:;
%%LST VLRUSRNUMCHECK:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
VLR非短信用户数核查开关= 打开
VLR非短信用户数核查速率 (个每秒) = 20
VLR非短信用户数核查周 期(小时) = 168

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLRUSRNUMCHECK.md`
