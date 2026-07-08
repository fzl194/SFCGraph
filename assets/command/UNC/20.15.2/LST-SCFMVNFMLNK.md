---
id: UNC@20.15.2@MMLCommand@LST SCFMVNFMLNK
type: MMLCommand
name: LST SCFMVNFMLNK（查询超时时间配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCFMVNFMLNK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# LST SCFMVNFMLNK（查询超时时间配置）

## 功能

该命令用于查询VNFM-VNF之间同步消息超时时间配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCFMVNFMLNK]] · 超时时间配置（SCFMVNFMLNK）

## 使用实例

LST SCFMVNFMLNK

```
%%LST SCFMVNFMLNK:;%%
RETCODE = 0  操作成功

结果如下
------------------------
同步消息超时时间  =  180
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCFMVNFMLNK.md`
