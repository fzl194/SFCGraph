---
id: UDG@20.15.2@MMLCommand@ADD SRVCERTSCENE
type: MMLCommand
name: ADD SRVCERTSCENE（增加配置证书场景）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SRVCERTSCENE
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继证书场景
status: active
---

# ADD SRVCERTSCENE（增加配置证书场景）

## 功能

**适用NF：UPF、PGW-U**

该命令用于增加配置证书场景。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 当用户不输入CNDESC、 ENDESC时，会将SCENE的值赋给未输入的CNDESC、ENDESC。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 证书使用场景名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。区分大小写，不允许仅大小写不同的重复记录。不支持中文字符，只能由“_”、数字和大小写字母组成。<br>默认值：无<br>配置原则：无 |
| TYPE | 场景类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示证书使用场景类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SCENE_CA：CA证书场景类型。<br>- SCENE_NE：设备证书场景类型。<br>默认值：无<br>配置原则：无 |
| CNDESC | 证书使用场景中文描述 | 可选必选说明：可选参数<br>参数含义：证书使用场景中文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ENDESC | 证书使用场景英文描述 | 可选必选说明：可选参数<br>参数含义：证书使用场景英文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [配置证书场景（SRVCERTSCENE）](configobject/UDG/20.15.2/SRVCERTSCENE.md)

## 使用实例

新增配置证书场景：

```
ADD SRVCERTSCENE: SCENE="test01", TYPE=SCENE_CA;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加配置证书场景（ADD-SRVCERTSCENE）_94632037.md`
