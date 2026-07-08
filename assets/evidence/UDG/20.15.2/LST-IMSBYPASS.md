# 显示IMS Bypass功能的相关参数（LST IMSBYPASS）

- [命令功能](#ZH-CN_CONCEPT_0000204208806803__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000204208806803__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000204208806803__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000204208806803__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000204208806803__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000204208806803)

**适用NF：PGW-U、UPF**

该命令用于查询IMS Bypass功能的相关参数。

#### [注意事项](#ZH-CN_CONCEPT_0000204208806803)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000204208806803)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000204208806803)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000204208806803)

使用LST IMSBYPASS命令查询IMS Bypass功能的相关参数：

```
LST IMSBYPASS:;
```

```

RETCODE = 0  Operation succeeded

List IMS QoS URR reporting parameters
-------------------------------------
                        IMS Bypass switch  =  Disable
         URR-based QoS Flow Report Method  =  FLOW
Hysteresis Time for QoS type URR Stop (s)  =  0
(Number of results = 1)

---    END
```
