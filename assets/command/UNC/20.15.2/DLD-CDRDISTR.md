---
id: UNC@20.15.2@MMLCommand@DLD CDRDISTR
type: MMLCommand
name: DLD CDRDISTR（下载SFTP密钥文件到本端）
nf: UNC
version: 20.15.2
verb: DLD
object_keyword: CDRDISTR
command_category: 调测类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单分发
status: active
---

# DLD CDRDISTR（下载SFTP密钥文件到本端）

## 功能

**适用NF：NCG**

登录OM Portal，通过文件传输服务上传密钥文件，执行该命令可以将密钥文件从OM Portal下载到业务容器上，并成功加载。

## 注意事项

- 必须先上传密钥文件到OM Portal，否则命令执行失败。
- 密钥文件名必须和分发任务名一致。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDISTRID | 分发任务标识 | 可选必选说明：必选参数<br>参数含义：分发任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数由增加话单分发(<br>[**ADD CDRDISTR**](增加话单分发（ADD CDRDISTR）_51174254.md)<br>)命令添加；可使用查询话单分发(<br>[**LST CDRDISTR**](查询话单分发（LST CDRDISTR）_51174257.md)<br>)命令查询。 |

## 操作的配置对象

- [上传SFTP密钥文件到BS侧（CDRDISTR）](configobject/UNC/20.15.2/CDRDISTR.md)

## 使用实例

下载密钥文件到“cdrdistr_pull”任务开放给BS侧的目录下：

```
DLD CDRDISTR: CDRDISTRID="cdrdistr_pull";
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/下载SFTP密钥文件到本端（DLD-CDRDISTR）_51174253.md`
