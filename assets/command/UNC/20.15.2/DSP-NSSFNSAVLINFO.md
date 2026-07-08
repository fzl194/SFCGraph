---
id: UNC@20.15.2@MMLCommand@DSP NSSFNSAVLINFO
type: MMLCommand
name: DSP NSSFNSAVLINFO（显示切片可用性信息概要信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFNSAVLINFO
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFNSAVLINFO（显示切片可用性信息概要信息）

## 功能

**适用NF：NSSF**

该命令用于查询切片可用性信息：

若要查询全部切片可用性信息，请不要输入任何参数；若要查询指定AMF上报的可用性信息，请输入对应的AMF实例标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFINSTANCEID | AMF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示AMF实例标识，若需要查询指定的AMF上报的可用性信息，可通过该参数配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFNSAVLINFO]] · 切片可用性信息（NSSFNSAVLINFO）

## 使用实例

运营商想要查询切片可用性信息概要信息时，执行此命令。

```
查询全部切片可用性信息：
%%DSP NSSFNSAVLINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
AMF实例标识    AMF集合标识    TAI数目         切片总数目(每个TAI下切片数目之和)  

uuid3          460-03-01-002  1               3                                                            
uuid1          460-03-01-001  1               3                                                            
(结果个数 = 2)

---    END

查询指定AMF上报的可用性信息：
%%DSP NSSFNSAVLINFO: AMFINSTANCEID="uuid3";%%
RETCODE = 0  操作成功

结果如下
------------------------
                      AMF实例标识  =  uuid3
                      AMF集合标识  =  460-03-01-002
                          TAI数目  =  1
切片总数目(每个TAI下切片数目之和)  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示切片可用性信息概要信息（DSP-NSSFNSAVLINFO）_96241982.md`
