# 下载SFTP密钥文件到本端（DLD CDRDISTR）

- [命令功能](#ZH-CN_CONCEPT_0251174253__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174253__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174253__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174253__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174253__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174253__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174253)

**适用NF：NCG**

登录OM Portal，通过文件传输服务上传密钥文件，执行该命令可以将密钥文件从OM Portal下载到业务容器上，并成功加载。

#### [注意事项](#ZH-CN_CONCEPT_0251174253)

- 必须先上传密钥文件到OM Portal，否则命令执行失败。
- 密钥文件名必须和分发任务名一致。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174253)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174253)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174253)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDISTRID | 分发任务标识 | 可选必选说明：必选参数<br>参数含义：分发任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数由增加话单分发(<br>[**ADD CDRDISTR**](增加话单分发（ADD CDRDISTR）_51174254.md)<br>)命令添加；可使用查询话单分发(<br>[**LST CDRDISTR**](查询话单分发（LST CDRDISTR）_51174257.md)<br>)命令查询。 |

#### [使用实例](#ZH-CN_CONCEPT_0251174253)

下载密钥文件到“cdrdistr_pull”任务开放给BS侧的目录下：

```
DLD CDRDISTR: CDRDISTRID="cdrdistr_pull";
RETCODE = 0  操作成功

---    END
```
