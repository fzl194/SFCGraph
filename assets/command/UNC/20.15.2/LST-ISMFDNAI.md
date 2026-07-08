---
id: UNC@20.15.2@MMLCommand@LST ISMFDNAI
type: MMLCommand
name: LST ISMFDNAI（查询I-SMF支持的DNAI）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ISMFDNAI
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI管理
- I-SMF DNAI管理
status: active
---

# LST ISMFDNAI（查询I-SMF支持的DNAI）

## 功能

**适用NF：SMF**

该命令用于查询I-SMF支持的DNAI。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识符 | 可选必选说明：可选参数<br>参数含义：该参数用于指定I-SMF支持的DNAI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ISMFDNAI]] · I-SMF支持的DNAI（ISMFDNAI）

## 使用实例

查询DNAI为“huawei.com.dnai”的I-SMF DNAI，运行以下命令：

```
%%LST ISMFDNAI: DNAI="huawei.com.dnai";%%
RETCODE = 0  操作成功

结果如下
------------------------
            数据网络访问标识符  =  huawei.com.dnai
                      DNAI类型  =  DNN级别
                           DNN  =  huawei.com
仅使用DNAI查询辅锚点的控制开关  =  使能
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ISMFDNAI.md`
