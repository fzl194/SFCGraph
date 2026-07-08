---
id: UDG@20.15.2@MMLCommand@LST VNFPODVM
type: MMLCommand
name: LST VNFPODVM（查询网元的POD与虚拟机位置关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VNFPODVM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# LST VNFPODVM（查询网元的POD与虚拟机位置关系）

## 功能

查询网元对应的POD与虚拟机位置关系。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| VNFID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VNFPODVM]] · 网元的POD与虚拟机位置关系（VNFPODVM）

## 使用实例

查询网元ID为0的POD对应虚拟机位置关系信息。

```
%%LST VNFPODVM: VNFID=0;%%
RETCODE = 0  操作成功

操作结果如下
------------
网元ID 网元类型  Pod ID                                 POD类型             POD所在虚拟机的虚拟机ID               虚拟机类型  POD名称

0      APP       9acfacda-522a-11ea-b3b5-fa163eb9ce89  patchmg             33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       patchmgr-79bbdcd99d-gvasdsl
0      APP       9ad7c0bb-522a-11ea-b3b5-fa163eb9ce89  patchmg             f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       patchmgr-79bbdcd99d-gvafdsl
0      APP       d7615d4a-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  c387ae41-d5fc-4655-9d21-63f002684ccb  APP_B       cse-service-center-8867c8f8-512dsfr
0      APP       d76a8b5b-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       cse-service-center-8867c8f8-5terv8r
0      APP       d76a7840-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       cse-service-center-8867c8f8-5tvdf8r
0      APP       baf43e7e-522a-11ea-b3b5-fa163eb9ce89  filetrans           f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       filetransfer-5cb94d646-52saqlg
0      APP       baee0778-522a-11ea-b3b5-fa163eb9ce89  filetrans           33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       filetransfer-5cb94d646-52qaslg
0      APP       cda377a3-522a-11ea-b3b5-fa163eb9ce89  omce                f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       omce-5cba94d646-52sdqlg
0      APP       102bc6f3-522c-11ea-b3b5-fa163eb9ce89  omce                33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       omce-5cba94d646-52asqlg

(结果个数 = 9)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网元的POD与虚拟机位置关系（LST-VNFPODVM）_26089554.md`
