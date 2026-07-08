---
id: UNC@20.15.2@MMLCommand@LST NSDNN
type: MMLCommand
name: LST NSDNN（查询网络切片支持的DNN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSDNN
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 网络切片内DNN管理
status: active
---

# LST NSDNN（查询网络切片支持的DNN）

## 功能

**适用NF：SMF**

该命令用于查询网络切片支持的DNN列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIDX | 网络切片索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络切片，可以使用LST PLMNNS命令查询获取。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>本参数通过ADD NFNS命令进行配置，且NF类型必须是NfSMF。 |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。可配置通配DNN，即“*”，表示支持所有DNN。<br>默认值：无<br>配置原则：<br>确保为S-NSSAI增加其支持的DNN在LST APN中能够查询到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSDNN]] · 网络切片支持的DNN（NSDNN）

## 使用实例

查询eMBB切片支持的DNN列表：

```
%%LST NSDNN: NSIDX=0, DNN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
         网络切片索引  =  0
         数据网络名称  =  huawei.com
EPS互操作默认切片指示  =  否
绑定的SMFINFO ID = null
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网络切片支持的DNN（LST-NSDNN）_09652609.md`
