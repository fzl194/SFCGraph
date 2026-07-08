---
id: UNC@20.15.2@MMLCommand@RMV NGTANEIBCFG
type: MMLCommand
name: RMV NGTANEIBCFG（删除TA邻接关系配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGTANEIBCFG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- TA邻接关系管理
status: active
---

# RMV NGTANEIBCFG（删除TA邻接关系配置）

## 功能

**适用NF：AMF**

此命令用于删除手动添加的TA站邻接关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | TA标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心跟踪区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位十进制数字，MNC为2位或者3位十进制数字，填写时请遵循实际长度。TAC编码为十六进制数，长度固定为6位；若不足则左起用0补足6位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TA邻接关系配置（NGTANEIBCFG）](configobject/UNC/20.15.2/NGTANEIBCFG.md)

## 使用实例

在完成“邻接TA”范围的精准寻呼测试后，删除一条手动添加的TA邻接关系，其中心TA的标识TAI为"12345100010"，执行如下命令：

```
RMV NGTANEIBCFG: TAI="12345100010";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除TA邻接关系配置（RMV-NGTANEIBCFG）_76181743.md`
