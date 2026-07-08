---
id: UNC@20.15.2@MMLCommand@DSP UPDSTATUS
type: MMLCommand
name: DSP UPDSTATUS（显示升级状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPDSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# DSP UPDSTATUS（显示升级状态）

## 功能

该命令用于显示RU升级状态。

## 注意事项

RU状态是offline且后台进程正常时，RU升级状态查询结果不是Null。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| STATUS | 状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示升级状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- On：开始升级。<br>- Off：结束升级。<br>- Null: 单板状态未知。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [升级状态（UPDSTATUS）](configobject/UNC/20.15.2/UPDSTATUS.md)

## 使用实例

显示RU升级状态：

```
DSP UPDSTATUS:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功 

结果如下:  
-------------------------  
RU名称                     状态
VNODE_UGW_VNFC_OMU_0001    升级结束
VNODE_UGW_VNFC_OMU_0002    升级结束
VNODE_UGW_VNFC_SPU_0064    升级结束
VNODE_UGW_VNFC_SPU_0065    升级结束
(结果个数 = 4)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示升级状态（DSP-UPDSTATUS）_88089822.md`
