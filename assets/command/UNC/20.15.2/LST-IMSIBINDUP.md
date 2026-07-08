---
id: UNC@20.15.2@MMLCommand@LST IMSIBINDUP
type: MMLCommand
name: LST IMSIBINDUP（查询用户和UPF的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIBINDUP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户绑定UPF
status: active
---

# LST IMSIBINDUP（查询用户和UPF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询用户和UPF的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [用户和UPF的绑定关系（IMSIBINDUP）](configobject/UNC/20.15.2/IMSIBINDUP.md)

## 使用实例

显示所有用户UPF的绑定关系： LST IMSIBINDUP:;

```
%%LST IMSIBINDUP:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
起始IMSI         终止IMSI         接入类型   主锚点UPF实例名称  辅锚点UPF实例名称  N3/S1-U口UPF实例名称  ULCL部署模式         重选到绑定UPF  重选指向的辅锚点UPF实例名称  重选指向的接入UPF实例名称  重选后的ULCL部署模式  智能分流专用会话锚点UPF实例名称

111111000000000  111111999999999  5G接入     up1                up2                up3                   优先使用辅锚点分流   开             up4                          up5                        优先使用辅锚点分流    up6
211111000000000  211119999999999  5G接入     up1                up2                up3                   只使用主锚点分流     开             up4                          up5                        只使用主锚点分流      up6
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户和UPF的绑定关系（LST-IMSIBINDUP）_09651580.md`
