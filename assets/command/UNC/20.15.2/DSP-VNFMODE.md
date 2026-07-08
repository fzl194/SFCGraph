---
id: UNC@20.15.2@MMLCommand@DSP VNFMODE
type: MMLCommand
name: DSP VNFMODE（查询VNF部署模式）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VNFMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP VNFMODE（查询VNF部署模式）

## 功能

该命令用于查询VNF部署模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFMODE]] · VNF部署模式（VNFMODE）

## 使用实例

查询VNF部署模式。

```
%%DSP VNFMODE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
VNF容器模式  =  VM_CONTAINER
裸机部署模式  =  DomainHost
Vnfm接口模式 =  stack
附加模式     =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-VNFMODE.md`
