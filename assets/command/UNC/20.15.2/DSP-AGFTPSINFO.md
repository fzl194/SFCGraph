---
id: UNC@20.15.2@MMLCommand@DSP AGFTPSINFO
type: MMLCommand
name: DSP AGFTPSINFO（显示AGF每个pod的计费消息速率）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AGFTPSINFO
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF计费消息速率信息
status: active
---

# DSP AGFTPSINFO（显示AGF每个pod的计费消息速率）

## 功能

**适用NF：NCG**

该命令用于显示AGF每个pod的计费消息速率。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64，单位是个。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AGFTPSINFO]] · AGF每个pod的计费消息速率（AGFTPSINFO）

## 使用实例

显示AGF每个pod的计费消息速率。

```
DSP AGFTPSINFO:;
RETCODE = 0  操作成功

结果如下
--------
          Pod名称  =  ccp-pod
计费消息速率(TPS)  =  666
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AGFTPSINFO.md`
