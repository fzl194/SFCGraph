---
id: UNC@20.15.2@MMLCommand@LST SPECRFSPVALUE
type: MMLCommand
name: LST SPECRFSPVALUE（查询特征RFSP取值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SPECRFSPVALUE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- RFSP管理
- 特征RFSP管理
- 特征RFSP取值范围管理
status: active
---

# LST SPECRFSPVALUE（查询特征RFSP取值）

## 功能

**适用网元：SGSN、MME**

该命令用于查询特征RFSP(RAT/Frequency Selection Priority)的取值范围。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RFSPIDX | 特征RFSP索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定特征RFSP索引，该索引标识了一组或多组RFSP取值。<br>取值范围：0~49<br>默认值：无 |
| TYPE | 特征RFSP索引类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该特征RFSP索引的类型。<br>取值范围：<br>- “IMS_VOPS(IMS VoPS限制)”：表示该特征RFSP范围用于IMS VoPS限制。<br>- “ENODEB_IND(eNodeB指示)”：表示该特征RFSP范围用于将签约RFSP ID映射成SPID。<br>- “ACC_REJECT(区域接入控制)”：表示该特征RFSP范围用于区域接入控制。<br>默认值：无 |
| RFSP | RFSP | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个待查询的RFSP值。<br>取值范围：1~256<br>默认值：无<br>说明：如果指定该参数，则会将所有满足该RFSP值在起始RFSP和终止RFSP之间的所有结果输出，起始RFSP和终止RFSP为通过<br>[**ADD SPECRFSPVALUE**](增加特征RFSP取值(ADD SPECRFSPVALUE)_26145534.md)<br>命令添加的两个参数。 |

## 操作的配置对象

- [特征RFSP取值（SPECRFSPVALUE）](configobject/UNC/20.15.2/SPECRFSPVALUE.md)

## 使用实例

查询特征RFSP(RAT/Frequency Selection Priority)的取值范围：

LST SPECRFSPVALUE:;

```
%%LST SPECRFSPVALUE:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
    特征RFSP索引  =  0
特征RFSP索引类型  =  区域接入控制
        起始RFSP  =  1
        终止RFSP  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询特征RFSP取值(LST-SPECRFSPVALUE)_26305346.md`
