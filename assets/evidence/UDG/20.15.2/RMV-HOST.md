# 删除Host（RMV HOST）

- [命令功能](#ZH-CN_CONCEPT_0186528750__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186528750__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186528750__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186528750__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186528750__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186528750)

**适用NF：PGW-U、UPF**

RMV HOST此命令用来删除指定Host主机名或所有Host主机名。

#### [注意事项](#ZH-CN_CONCEPT_0186528750)

- 该命令执行后立即生效。
- 在删除Host信息执行RMV HOST命令前，需要确定HostName是否被Filter对象引用，如已绑定需先解除绑定后执行RMV HOST命令。
- 输入HostName删除指定配置。不输入HostName进行删除，执行一次删除命令最多删除5000条配置。
- 通过 ADD FILTER 或 MOD FILTER 中的参数Host配置名称可以解绑Host，最后一个解绑的Host生效时间为60s，其他解绑立刻生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0186528750)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186528750)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | Host配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HOST配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186528750)

删除Host主机名称，主机名为“huawei”：

```
RMV HOST:HOSTNAME="huawei";
```
